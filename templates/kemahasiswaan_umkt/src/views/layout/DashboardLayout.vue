<template>
  <div>
     <div class="flex w-full">
        <NavbarDashComponent />
        <div class="min-h-screen w-full px-10 py-5">
          <router-view></router-view>
        </div>
    </div>
  </div>
</template>

<script>
import NavbarDashComponent from "@/components/layout/NavbarDashComponent";

export default {
  name: "DashboardLayout",
  components: {
    NavbarDashComponent
  }

}
</script>

<style scoped>

</style>