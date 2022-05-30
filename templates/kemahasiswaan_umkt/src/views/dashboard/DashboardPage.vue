<template>
  <div>
    <div class="grid grid-cols-12 gap-x-5 gap-y-5 my-5">
      <MacCardComponent cardsname="Staff | Status" class="row-span-2 col-span-6 overflow-hidden">
        <div class="">
          <BarChartComponent :chart-data="{'labels': ['test', 'test2', 'test3', 'test4'], 'datasets': [{ 'data': [200, 20, 12, 20, 12] }]}" :chart-options="{responsive: true,maintainAspectRatio: false,'indexAxis': 'y'}"/>
        </div>
      </MacCardComponent>
      <MacCardComponent cardsname="Staff | Status" class="row-span-1 col-span-6 overflow-hidden">
        <div class="">
          <BarChartComponent :chart-data="{'labels': ['test', 'test2', 'test3', 'test4'], 'datasets': [{ 'data': [200, 20, 12, 20, 12] }]}" :chart-options="{responsive: true,maintainAspectRatio: false,'indexAxis': 'y'}" :height="300"/>
        </div>
      </MacCardComponent>
      <MacCardComponent cardsname="Staff | Status" class="row-span-1 col-span-6 overflow-hidden">
        <div class="">
          <BarChartComponent :chart-data="{'labels': ['test', 'test2', 'test3', 'test4'], 'datasets': [{ 'data': [200, 20, 12, 20, 12] }]}" :chart-options="{responsive: true,maintainAspectRatio: false,'indexAxis': 'y'}" :height="300"/>
        </div>
      </MacCardComponent>
    </div>
  </div>
</template>

<script>
import MacCardComponent from "@/components/widget/MacCardComponent";
import BarChartComponent from "@/components/chart/BarChartComponent";
export default {
  name: "DashboardPage",
  components: {
    BarChartComponent,
    MacCardComponent
  }
}
</script>

<style scoped>

</style>