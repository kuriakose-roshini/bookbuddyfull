am4core.options.commercialLicense = true;

function am4themes_cs(target) {
  if (target instanceof am4core.ColorSet) {
    target.list = [
      am4core.color("#2876BC"),
      am4core.color("#1FBCFF"),
      am4core.color("#00B800"),
      am4core.color("#83CE00"),
      am4core.color("#FEE83F"),
      am4core.color("#FFCF00"),
      am4core.color("#FFA500"),
      am4core.color("#FF7D00"),
      am4core.color("#EE5A30"),
      am4core.color("#D046B6"),                                                                     
      am4core.color("#653789"),
      am4core.color("#2A49A0")
    ];
  }
  if (target instanceof am4core.Tooltip) {
    target.getFillFromObject = false;
    target.getStrokeFromObject = false;
    target.background.strokeOpacity = 0.4;
    target.background.fill = am4core.color("#000");
  }
  if (target instanceof am4core.Label) {
    target.fill = am4core.color("#555");
  }
  if (target instanceof am4charts.Axis) {
    target.cursorTooltipEnabled = false;
  }
  if (target instanceof am4charts.AxisRendererY) {
    target.grid.template.strokeOpacity = 0;
    // target.line.strokeOpacity = 1;
  }
  if (target instanceof am4charts.Grid) {
    target.strokeOpacity = 0.1;
    target.stroke = am4core.color("#000");
  }
  if (target instanceof am4core.InterfaceColorSet) {
    target.setFor("text", am4core.color("#333"));
    target.setFor("primaryButton", am4core.color("#666"));
    target.setFor("primaryButtonHover", am4core.color("#1FBCFF"));
    target.setFor("primaryButtonDown", am4core.color("#1FBCFF").lighten(-0.2));
    target.setFor(
      "primaryButtonActive",
      am4core.color("#1FBCFF").lighten(-0.2)
    );

  }
}

am4core.useTheme(am4themes_cs);

var data = [
  {
    id: 10001,
    name: "Most taken books by members",
    count: 15,
    children: [
      { id: 10002, name: "Advanced Data Stuctures", count: 4 },
      { id: 10003, name: "API", count: 3 },
      { id: 10004, name: "Artificial Intelligence", count: 5 },
      { id: 10005, name: "Automata Theory", count: 2 },
    ]
  },
  {
    id: 10006,
    name: "Most taken books of the month",
    count: 15,
    children: [
      { id: 10007, name: "API", count: 4 },
      { id: 10008, name: "Java for beginners", count: 7 },
      { id: 10009, name: "Operating Systems", count: 2 },
      { id: 10010, name: "Computer Vision", count: 2 },
    ]
  },
  
];

// create chart
var piechart = am4core.create("chartdiv", am4charts.PieChart);
piechart.data = data;
piechart.maskBullets = false;
piechart.padding(am4core.percent(0), 120, am4core.percent(0), 120);
piechart.margin(0, 0, 0, 0);
// piechart.innerRadius = am4core.percent(0);

var series = piechart.series.push(new am4charts.PieSeries());
series.dataFields.value = "count";
series.dataFields.category = "name";
series.dataFields.children = "children";
series.labels.template.maxWidth = 150;
series.labels.template.wrap = true;
// series.labels.template.text = "[bold]{category}:[/] {percent}";

var slicehover = series.slices.template.states.create("hover");

slicehover.properties.shiftRadius = 0;
slicehover.properties.scale = 1;
slicehover.properties.fillOpacity = 1;

series.slices.template.events.on("hit", function(ev) {

    //setup single select
    var series = ev.target.dataItem.component;
    series.slices.each(function(item) {
      if (item.isActive && item != ev.target) {
        item.isActive = false;
      }
    });
    
    reasonsActiveLocal = [];

    // this eventually needs to loop through active[] elements
    var catName = ev.target.dataItem.dataContext.name;
    var catValues =
      Math.round(ev.target.dataItem.values.value.percent * 10) / 10 +
      "% (" +
      ev.target.dataItem.values.value.value +
      ")";

    updateCatTitle(catName, catValues);
  
    barchart.invalidateData();
    barchart.data = [];
    barchart.data = ev.target.dataItem.dataContext.children;
    console.log('bardata items', ev.target.dataItem.dataContext.children.length);

    barSeries.columns.template.fill = ev.target.fill;
    barSeries.columns.template.stroke = ev.target.fill;
  },
  this
);

var barchart = am4core.create("barchart", am4charts.XYChart);
// barchart.paddingRight = 0;
barchart.paddingLeft = 0;
barchart.zoomOutButton.disabled = true;

barchart.data = data[0].children;

barchart.adapter.add("data", function(data) {
  data.sort(function(a, b) {
    return a.count - b.count;
  });
  return data;
});

var catAxis = barchart.yAxes.push(new am4charts.CategoryAxis());
catAxis.dataFields.category = "name";
catAxis.renderer.minGridDistance = 1;
catAxis.renderer.grid.template.location = 0;
catAxis.renderer.labels.template.align = "left";
catAxis.renderer.labels.template.maxWidth = 200;
catAxis.renderer.labels.template.truncate = true;
catAxis.renderer.labels.template.tooltipText = "{category}";

var valAxis = barchart.xAxes.push(new am4charts.ValueAxis());
valAxis.min = 0;
valAxis.maxPrecision = 0;
valAxis.renderer.opposite = true;

var barSeries = barchart.series.push(new am4charts.ColumnSeries());
barSeries.dataFields.valueX = "count";
barSeries.dataFields.categoryY = "name";
barSeries.columns.template.height = 20;

var bullet = barSeries.bullets.push(new am4charts.LabelBullet());
bullet.label.dx = 10;
bullet.label.text = "[bold]{valueX}[/]";
bullet.label.horizontalCenter = "left";
bullet.label.textAlign = "left";

function updateCatTitle(title, stats) {
  var catHeaderText = document.getElementById("cat-header-text");
  var catHeaderStats = document.getElementById("cat-header-stats");
  catHeaderText.innerHTML = title;
  catHeaderStats.innerHTML = stats;
}

var defaultState = barSeries.columns.template.states.create("default");

var activeState = barSeries.columns.template.states.create("active");
activeState.properties.strokeOpacity = 1;
activeState.properties.strokeWidth = 1;
activeState.properties.fillOpacity = 1;

var notSelected = barSeries.columns.template.states.create("notSelected");
notSelected.properties.fillOpacity = 0.2;
notSelected.properties.strokeOpacity = 0.2;

// Auto adjust container height based on # of data items
var cellSize = 43;
var reasonsActiveLocal = [];

barchart.events.on("datavalidated", function(ev) {
  console.log("barchart datavalidated");
  // Get objects of interest
  var chart = ev.target;
  var categoryAxis = chart.yAxes.getIndex(0);

  // Calculate how we need to adjust chart height
  var adjustHeight = chart.data.length * cellSize - categoryAxis.pixelHeight;
  // get current chart height
  var targetHeight = chart.pixelHeight + adjustHeight;

  console.log("chart height",chart.svgContainer.htmlElement.offsetHeight);
  console.log("chart chunks",chart.svgContainer.htmlElement.offsetHeight/cellSize);
  console.log("chart target height", targetHeight);
  if (targetHeight > 550) {
    console.log("add scrollbar");
    chart.scrollbarY = new am4core.Scrollbar();
    chart.scrollbarY.hideGrips = true;
    // Set height on chart's container
    chart.svgContainer.htmlElement.style.height = targetHeight + "px";
    chart.mouseWheelBehavior = "panY";
    categoryAxis.zoomToIndexes(chart.data.length - 12, chart.data.length);
  } else {
    console.log("chart new height", targetHeight);
    // Set it on chart's container
    chart.svgContainer.htmlElement.style.height = targetHeight + "px";
    chart.scrollbarY = false;
    categoryAxis.zoomToIndexes(0, chart.data.length);
    chart.mouseWheelBehavior = "none";
  }
  
  console.log(ev.target.data);

});

barSeries.columns.template.events.on("toggled", function(ev) {

  console.log("hit event");

  var currentId = ev.target.dataItem.dataContext.id;
  console.log("ev id", currentId);

  if (reasonsActiveLocal.includes(currentId) && !ev.target.isActive) {
    var itemIndex = reasonsActiveLocal.indexOf(currentId);
    reasonsActiveLocal.splice(itemIndex, 1);
  } else if (ev.target.isActive) {
    reasonsActiveLocal.push(currentId);
  }

  console.log("reasons active", reasonsActiveLocal);
  console.log("reasonSeries items", barSeries.columns.length);
  console.log("barchart items", barchart.data.length);
  console.log("barchart component", ev.target.dataItem.component.columns.length);

  barSeries.columns.each(function(column) {

    // if(!column.isDisposed()){
      if (reasonsActiveLocal.length > 0) {
        if (!reasonsActiveLocal.includes(column.dataItem.dataContext.id)) {
          //console.log("set notSelected state", column.dataItem.dataContext.id);
          column.setState("notSelected");
          column.isActive = false;
        } else {
          //console.log("set active state", column.dataItem.dataContext.id);
          column.setState("active");
          column.isActive = true;
        }
      } else {
        console.log("set default state");
        column.defaultState.properties.fillOpacity = 1;
        column.setState("default");
        column.isActive = false;
      }
    // } else {
    //   console.log('dispose column');
    //   column.dispose();
    // }
  });
});