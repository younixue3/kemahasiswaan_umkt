<template>
  <div>
    <div class="grid grid-cols-12 gap-x-5 gap-y-5 my-5">
      <MacCardComponent cardsname="Staff | Status" class="col-span-12 overflow-hidden">
        <table class="table-auto w-full text-xs md:text-base mb-4">
          <thead class="border-b-4">
          <tr>
            <th>No</th>
            <th>Mahasiswa</th>
            <th>Event</th>
            <th>Penyelenggara</th>
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
import axios from "axios";

export default {
  name: "ListPrestasiPage",
  components: {
    MacCardComponent
  },
  data() {
    return {
      data: null,
    }
  },
  methods: {
    getList: function () {
      axios.get(process.env.VUE_APP_BASE_URL + "/prestasi/get_list")
          .then(resp => {
            console.log(resp)
          })
    }
  }
}
</script>

<style scoped>

</style>