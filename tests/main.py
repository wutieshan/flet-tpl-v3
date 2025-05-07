from highcharts_core.chart import Chart

chart = Chart(data=[0, 5, 3, 5, 10, 7, 8, 9, 6], series_type="line", container="container")
tags = chart.get_script_tags()
js = chart.to_js_literal()


html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <title>Highcharts gantt</title>
  <meta charset="utf-8">
</head>
<body>
{'\n'.join(tags)}
<div id="container"></div>
<script>
{js}
</script>
</body>
</html>
"""

with open("index.html", "w+", encoding="utf8") as fp:
    fp.write(html)
