var ec_center = echarts.init(document.getElementById('China'));

var mydata = [{'name': '上海', 'value': 318},{"name": "云南", "value": 162}];

var ec_center_option = {
	title: {
		text: "",
		subtext: "",
		x: 'left'
	},
	tooltip: {
		trigger: "item"
	},
	//左侧小导航图标
	visualMap: {
		show: true,
		x: "left",
		y: 'bottom',
		textStyle: {
			fontSize: 8
		},
		splitList: [
			{start: 1, end: 9},
			{start: 100, end: 999},
			{start: 1000, end: 9999},
			{start: 10000}
		],
		color: ['#8A3300', "#C64918", "#E55825", "#F2AD92", "#F9DCD1"]
	},
	series: [{
		name: '商家',
		type: "map",
		mapType: "china",
		roam: false,
		itemStyle: {
			normal: {
				borderWidth: 0.5,
				borderColor: "#4b0082",
				areaColor: "#fff"
			}
		},
		label: {
			normal: {
				show: true,
				fontSize: 8
			},
			emphasis: {
				show: true,
				fontSize: 8
			}
		},
		data: mydata
	}]
};
ec_center.setOption(ec_center_option);