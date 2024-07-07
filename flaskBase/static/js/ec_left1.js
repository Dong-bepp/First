 var ec_left1 = echarts.init(document.getElementById('left1'));
		        var ec_left1_option = {
		          xAxis: {
		            type: 'category',
		            data: []  // 将data设置为空数组
		          },
		           yAxis: {
		              type: 'value',
		              axisLine: {
		                lineStyle: {
		                  color: 'white'  // Y轴线条颜色设置为白色
		                }
		              },
		              axisLabel: {
		                color: 'white'  // Y轴数字颜色设置为黑色
		              }
		            },
		          series: [
		            {
		              data: [820, 932, 901, 934, 1290, 1330, 1320],
					  
		              type: 'line',
		              smooth: true,
					  lineStyle: {
					          color: 'white'  // 将线条颜色设为白色
					        }
		            }
		          ]
		        };
		        ec_left1.setOption(ec_left1_option);