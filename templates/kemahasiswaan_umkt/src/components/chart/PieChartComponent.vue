<template>
  <Pie :chart-data="chartData" :chart-options="chartOptions" :height="height"/>
</template>

<script>
import {Pie} from 'vue-chartjs/legacy'
import {Chart as ChartJS, Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale, ArcElement} from 'chart.js'

ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale, ArcElement)

export default {
  name: 'PieChartComponent',
  components: {Pie},
  props: {
    chartData: {
      type: Object,
      required: true
    },
    chartOptions: {
      type: Object,
      required: true
    },
    height: {
      type: Number,
      default: 400
    }
  }
}
</script>