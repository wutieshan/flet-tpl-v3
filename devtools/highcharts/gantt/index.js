// JS Api Reference: https://api.highcharts.com/gantt

Highcharts.ganttChart("container", {
  title: {
    align: "center",
    floating: false,
    margin: 15,
    minScale: 1,
    style: {},
    text: "highcharts-gantt",
    useHTML: true,
  },
  xAxis: {
    currentDateIndicator: false,
    grid: { enabled: false },
    labels: {
      enabled: true,
      format: "{value:%Y-%m-%d}",
    },
    tickInterval: 7 * 24 * 3600 * 1000, //Note: unit ms
    startOnTick: true,
    minPadding: 0.02,
    maxPadding: 0.06,
    type: "datetime",
    visible: true,
    opposite: false,
    dateTimeLabelFormats: {
      year: "%Y",
      month: "",
    },
  },
  series: [
    {
      name: "Project 1",
      data: [
        {
          name: "Task 1",
          start: Date.UTC(2025, 0, 1),
          end: Date.UTC(2025, 0, 15),
          completed: 0.5,
        },
        {
          name: "Task 2",
          start: Date.UTC(2025, 0, 16),
          end: Date.UTC(2025, 1, 15),
          completed: 0.2,
        },
      ],
    },
    {
      name: "Project 2",
      data: [
        {
          name: "Task 3",
          start: Date.UTC(2025, 1, 16),
          end: Date.UTC(2025, 2, 15),
          completed: 0.8,
        },
        {
          name: "Task 4",
          start: Date.UTC(2025, 2, 16),
          end: Date.UTC(2025, 2, 27),
          completed: 0.5,
        },
      ],
    },
  ],
  credits: { enabled: false },
});
