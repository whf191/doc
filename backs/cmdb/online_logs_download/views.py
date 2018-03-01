#coding=utf-8
from django.shortcuts import render_to_response,HttpResponse,HttpResponseRedirect
from django.http import StreamingHttpResponse
from .models import logsdownload
from .remote_paramiko.remote_paramiko import remote_paramiko
import logging,os
from django.utils.http import urlquote
from django.contrib.auth.decorators import login_required

hosts= {'crm':['192.168.0.106','grl9#^dm',22,'root'],'orderwildfly':['192.168.0.102','gb#9xg@v',22,'root'],
        'imgateway': ['192.168.0.42', '4yhjzt0r', 22, 'root']}

def get_local_dir():
    if not os.name == 'nt':
        local_dir = "/tmp/"
    else:
        local_dir = "d:/"
    return local_dir

logging.basicConfig(level=logging.DEBUG,
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                filename='online_logs_download.log',
                filemode='a')

def exec_cmd(project_name,cmd):
    pn = hosts.get(project_name,None)
    logging.info("exec_cmd:-->project_name:%s,cmd:%s" % (project_name,cmd))
    if pn and cmd:
        pn1  =hosts.get(project_name,None)
        rp = remote_paramiko(pn1[0],pn1[-1],pn[1],pn1[2])
        rp.call_log(logging.info)
        rp_cmd = rp.run(cmd)
        return rp_cmd

def get_sftp_cmd(project_name,remotefile,localfile):
    pn1 = hosts.get(project_name, None)
    logging.info("sftp_cmd-->project_name:%s,localfile:%s,remotefile:%s" % (project_name,localfile,remotefile ))
    rp = remote_paramiko(pn1[0], pn1[-1], pn1[1], pn1[2])
    rp.call_log(logging.info)
    rp.get_file(remotefile,localfile)
    return localfile

@login_required
def list_online_logs(request):
    if request.method == 'POST':
        pk = request.POST.get('pk',None)
        if pk:
            try:
                get_ld = logsdownload.objects.get(id=pk)
                project_name = get_ld.name
                rs_logs_dir = get_ld.log_dir
                rs_logs_dir = rs_logs_dir
                rs_logs_dir = "ls  -t  %s "  %  rs_logs_dir
                ec = exec_cmd(project_name,rs_logs_dir)
                logging.info("project_name:%s,result:%s" % (project_name,"".join(ec)))
                return HttpResponse(href(ec,project_name,pk))

            except Exception,e:
                logging.error("远程执行错误:%s" % e)
                return HttpResponse("远程执行错误")

    return HttpResponse("not post")


def file_iterator(file_name, chunk_size=4096):
    with open(file_name) as f:
        while True:
            c = f.read(chunk_size)
            if c:
                yield c
            else:
                break

@login_required
def get_online_log(request):
    if request.method =="GET":
        log1 = request.GET.get('log',None)
        pn1 = request.GET.get('pn',None)
        pk1  = request.GET.get('pk',None)
        if log1 and pn1 and pk1:
            get_ld = logsdownload.objects.get(id=pk1)
            remote_dir  = get_ld.log_dir
            remotefile= remote_dir + log1
            local_dir = get_local_dir()
            localfile = local_dir + pn1+"_"+log1
            rs = get_sftp_cmd(pn1,remotefile,localfile)
            downloadfile = rs.split("/")[-1]
            logging.info("downloadfile: %s" % downloadfile)
            tar_gz = "tar -zcf %s.tar.gz   %s  " % (downloadfile,downloadfile)
            os.chdir(local_dir)
            os.system(tar_gz)
            tarfile =  "%s.tar.gz" % downloadfile
            tarfile = local_dir + tarfile
            tarfile_name = tarfile.split("/")[-1]
            try:
                response = StreamingHttpResponse(file_iterator(tarfile))
                response['Content-Type'] = 'application/octet-stream'
                response['Content-Length'] = os.path.getsize(tarfile)
                response['Content-Disposition'] = 'attachment;filename=%s' % urlquote(tarfile_name)
                return response

            except:
                return HttpResponse("文件不存在")
        else:
            return HttpResponse("参数不对")

    return HttpResponse("not get")

def href(list1,projects_name,pk):
    html0 = ""
    html1= """
       <a href="/get_online_log/?log=%s&pn=%s&pk=%s">%s</a><br>
    """
    for i in list1:
        html0 += html1 % (i,projects_name,pk,i)

    return html0



