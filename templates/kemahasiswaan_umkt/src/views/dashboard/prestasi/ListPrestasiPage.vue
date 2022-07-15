<template>
  <div>
    <div class="grid grid-cols-12 gap-x-5 gap-y-5 my-5">
      <MacCardComponent cardsname="Staff | Status" class="col-span-12 overflow-hidden">
        <table class="table-auto w-full text-xs md:text-base mb-4">
          <thead class="border-b-4">
          <tr>
            <th>No</th>
            <th>Email</th>
            <th>Subject</th>
            <th>Date</th>
          </tr>
          </thead>
          <tbody>
          <tr class="border-b-2 border-gray-200 h-10">
            <td class="py-1"></td>
            <td class="truncate pl-3">
            </td>
            <td class="truncate">
            </td>
            <td class="truncate"></td>
          </tr>
          </tbody>
        </table>
      </MacCardComponent>
    </div>
  </div>
</template>

<script>
import MacCardComponent from "@/components/widget/MacCardComponent";

export default {
  name: "ListPrestasiPage",
  components: {
    MacCardComponent
  }
}
</script>

<style scoped>

</style>