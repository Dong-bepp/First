var ec_right2 = echarts.init(document.getElementById('right2'));
var ec_right2_option = {
  // backgroundColor: '#000000',
  title: {
    text: '店铺好评率',
    left: 'center',
    top: 20,
    textStyle: {
      color: 'white'
    }
  },
  tooltip: {
    trigger: 'item'
  },
  visualMap: {
    show: false,
    min: 80,
    max: 600,
    inRange: {
      colorLightness: [0, 1]
    }
  },
  series: [
    {
      name: '评价分布',
      type: 'pie',
      radius: '55%',
      center: ['50%', '50%'],
      data: [
        { value: 335, name: '4.8以上' },
        { value: 310, name: '4.5-4.8' },
        { value: 274, name: '4.0-4.5' },
        { value: 235, name: '3.5-4.0' },
        { value: 400, name: '3.5以下' }
      ].sort(function (a, b) {
        return a.value - b.value;
      }),
      roseType: 'radius',
      label: {
        color: 'white'
      },
      labelLine: {
        lineStyle: {
          color: 'rgba(255, 255, 255, 0.3)'
        },
        smooth: 0.2,
        length: 10,
        length2: 20
      },
      itemStyle: {
        color: '#c23531',
        shadowBlur: 200,
        shadowColor: 'rgba(0, 0, 0, 0.5)'
      },
      animationType: 'scale',
      animationEasing: 'elasticOut',
      animationDelay: function (idx) {
        return Math.random() * 200;
      }
    }
  ]
};
ec_right2.setOption(ec_right2_option)