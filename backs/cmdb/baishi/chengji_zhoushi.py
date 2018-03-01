#coding=utf-8
from __future__ import unicode_literals

tu = """
var title = {
      text: '成绩走势'
   };
   var subtitle = {
      text: '白市中学'
   };
   var xAxis = {
      categories: [%s]
   };
   var yAxis = {
      title: {
         text: '成绩走势'
      },
      plotLines: [{
         value: 0,
         width: 1,
         color: '#808080'
      }]
   };

   var tooltip = {
      valueSuffix: '分'
   }

   var legend = {
      layout: 'vertical',
      align: 'right',
      verticalAlign: 'middle',
      borderWidth: 0
   };

   var series =  [
      {
         name: '%s',
         data: %s
      }
   ];

   var json = {};

   json.title = title;
   json.subtitle = subtitle;
   json.xAxis = xAxis;
   json.yAxis = yAxis;
   json.tooltip = tooltip;
   json.legend = legend;
   json.series = series;











"""