<template>
  <Bar :chart-data="chartData" :chart-options="chartOptions" :width="width" :height="height"/>
</template>

<script>
import {Bar} from 'vue-chartjs/legacy'
import {Chart as ChartJS, Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale} from 'chart.js'

ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale)

export default {
  name: 'BarChartComponent',
  components: {Bar},
  props: {
    chartData: {
      type: Object,
      required: true
    },
    chartOptions: {
      type: Object,
      required: true
    },
    width: {
      type: Number,
      default: 400
    },
    height: {
      type: Number,
      default: 400
    }
  }
}
</script>