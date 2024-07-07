var ec_left2 = echarts.init(document.getElementById('left2'));
var list = [1048, 735, 580, 484, 300]
var ec_left2_option = {
  title: {
    text: '价格分布',
    textStyle: {
      color: 'white'
    },
    left: 'center',
    color: 'white'
  },
  tooltip: {
    trigger: 'item'
  },
  legend: {
    orient: 'vertical',
    left: 'left',
	 textStyle: {
	      color: 'white'
	    }
  },
  series: [
    {
      name: '价格分布',
      type: 'pie',
      radius: '50%',
      data: [
        { value: list[0], name: '1-50' },
        { value: list[1], name: '50-100' },
        { value: list[2], name: '100-150' },
        { value: list[3], name: '150-200' },
        { value: list[4], name: '200以上' }
      ],
      emphasis: {
        itemStyle: {
          shadowBlur: 10,
          shadowOffsetX: 0,
          shadowColor: 'rgba(0, 0, 0, 0.5)'
        }
      }
    }
  ]
};
ec_left2.setOption(ec_left2_option);