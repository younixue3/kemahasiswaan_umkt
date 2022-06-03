<template>
  <div>
    <div class="grid grid-cols-12 gap-x-5 gap-y-5 my-5">
      <MacCardComponent cardsname="Staff | Status" class="row-span-2 col-span-6 overflow-hidden">
        <div class="">
          <BarChartComponent :chart-data="{'labels': labeldata, 'datasets': [{label: 'Nilai Prestasi', 'data': prestasidata, backgroundColor: '#41B883' }]}" :chart-options="{responsive: true,maintainAspectRatio: false,'indexAxis': 'y'}"/>
        </div>
      </MacCardComponent>
      <MacCardComponent cardsname="Staff | Status" class="row-span-1 col-span-6 overflow-hidden">
        <div class="">
          <BarChartComponent :chart-data="{'labels': [''], 'datasets': jenisdata}" :chart-options="{responsive: true,maintainAspectRatio: false,'indexAxis': 'x'}" :height="300"/>
        </div>
      </MacCardComponent>
      <MacCardComponent cardsname="Staff | Status" class="row-span-1 col-span-6 overflow-hidden">
        <div class="">
          <PieChartComponent :chart-data="{'labels': ['test', 'test2', 'test3', 'test4'], 'datasets': [{label: 'Nilai Prestasi berdasarkan Prodi', 'data': [200, 20, 12, 20, 12], backgroundColor: ['#41B883', '#E46651', '#00D8FF', '#DD1B16', '#00DB17'] }]}" :chart-options="{responsive: true,maintainAspectRatio: false}" :height="400"/>
        </div>
      </MacCardComponent>
    </div>
  </div>
</template>

<script>
import MacCardComponent from "@/components/widget/MacCardComponent";
import BarChartComponent from "@/components/chart/BarChartComponent";
import PieChartComponent from "@/components/chart/PieChartComponent";
import axios from "axios";
export default {
  name: "DashboardPage",
  data() {
    return {
      labeldata: null,
      prestasidata: null,
      jenisdata: null
    }
  },
  components: {
    PieChartComponent,
    BarChartComponent,
    MacCardComponent
  },
  mounted() {
    this.topChartGet()
    this.jenisChartGet()
  },
  methods: {
    topChartGet: function () {
      axios.get(process.env.VUE_APP_BASE_URL + "/dashboard/top-chart-get")
      .then(resp => {
        this.labeldata = resp.data.label
        this.prestasidata = resp.data.data
      })
      .catch(e => console.log(e))
    },
    jenisChartGet: function () {
      axios.get(process.env.VUE_APP_BASE_URL + "/dashboard/jenis-chart-get")
      .then(resp => {
        this.jenisdata = resp.data.data
      })
      .catch(e => console.log(e))
    }
  }
}
</script>

<style scoped>

</style>