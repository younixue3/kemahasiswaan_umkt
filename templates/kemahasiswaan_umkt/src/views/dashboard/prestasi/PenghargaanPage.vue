<template>
  <div>
    <div class="grid grid-cols-12 gap-x-5 gap-y-5 my-5">
      <MacCardComponent cardsname="Staff | Status" class="col-span-12 overflow-hidden">
        <div class="grid grid-cols-2 gap-5 px-5">
          <div class="col-span-2">
            <label>Event</label>
            <div>
              <input class="bg-white w-full rounded-md py-2 pl-5 pr-3 shadow-sm focus:outline-none border border-gray-300 focus:border-sky-500 focus:ring-sky-500 focus:ring-1 font-semibold" type="text" name="event">
            </div>
          </div>
          <div class="col-span-2">
            <label>URL Kegiatan</label>
            <div>
              <input class="bg-white w-full rounded-md py-2 pl-5 pr-3 shadow-sm focus:outline-none border border-gray-300 focus:border-sky-500 focus:ring-sky-500 focus:ring-1 font-semibold" type="text" name="url_kegiatan">
            </div>
          </div>
          <div class="col-span-2">
            <label>Peyelenggara</label>
            <div>
              <input class="bg-white w-full rounded-md py-2 pl-5 pr-3 shadow-sm focus:outline-none border border-gray-300 focus:border-sky-500 focus:ring-sky-500 focus:ring-1 font-semibold" type="text" name="penyelenggara">
            </div>
          </div>
          <div>
            <label>Lingkup/Tingkat</label>
            <div>
              <input class="bg-white w-full rounded-md py-2 pl-5 pr-3 shadow-sm focus:outline-none border border-gray-300 focus:border-sky-500 focus:ring-sky-500 focus:ring-1 font-semibold" type="text" name="lingkup_tingkat">
            </div>
          </div>
          <div>
            <label>Jumlah Negara Peserta</label>
            <div>
              <input class="bg-white w-full rounded-md py-2 pl-5 pr-3 shadow-sm focus:outline-none border border-gray-300 focus:border-sky-500 focus:ring-sky-500 focus:ring-1 font-semibold" type="number" name="jumlah_negara">
            </div>
          </div>
          <div class="col-span-2">
            <label>Kategori</label>
            <div>
              <input class="bg-white w-full rounded-md py-2 pl-5 pr-3 shadow-sm focus:outline-none border border-gray-300 focus:border-sky-500 focus:ring-sky-500 focus:ring-1 font-semibold" type="text" name="kategori">
            </div>
          </div>
          <div>
            <label>Prestasi yang diraih</label>
            <div>
              <input class="bg-white w-full rounded-md py-2 pl-5 pr-3 shadow-sm focus:outline-none border border-gray-300 focus:border-sky-500 focus:ring-sky-500 focus:ring-1 font-semibold" type="text" name="prestasi_diraih">
            </div>
          </div>
          <div>
            <label>Ekuivalensi</label>
            <div>
              <input class="bg-white w-full rounded-md py-2 pl-5 pr-3 shadow-sm focus:outline-none border border-gray-300 focus:border-sky-500 focus:ring-sky-500 focus:ring-1 font-semibold" type="text" name="ekuivalensi">
            </div>
          </div>
          <div class="col-span-2">
            <label>Tempat</label>
            <div>
              <input class="bg-white w-full rounded-md py-2 pl-5 pr-3 shadow-sm focus:outline-none border border-gray-300 focus:border-sky-500 focus:ring-sky-500 focus:ring-1 font-semibold" type="text" name="tempat">
            </div>
          </div>
          <div>
            <label>Tanggal Mulai</label>
            <div>
              <input class="bg-white w-full rounded-md py-2 pl-5 pr-3 shadow-sm focus:outline-none border border-gray-300 focus:border-sky-500 focus:ring-sky-500 focus:ring-1 font-semibold" type="date" name="tanggal_mulai">
            </div>
          </div>
          <div>
            <label>Tanggal Selesai</label>
            <div>
              <input class="bg-white w-full rounded-md py-2 pl-5 pr-3 shadow-sm focus:outline-none border border-gray-300 focus:border-sky-500 focus:ring-sky-500 focus:ring-1 font-semibold" type="date" name="tanggal_selesai">
            </div>
          </div>
          <div class="col-span-2">
            <label>Deskripsi</label>
            <div>
              <textarea class="bg-white w-full rounded-md py-2 pl-5 pr-3 shadow-sm focus:outline-none border border-gray-300 focus:border-sky-500 focus:ring-sky-500 focus:ring-1 font-semibold" name="deskripsi"></textarea>
            </div>
          </div>
          <div>
            <label>Bukti</label>
            <div>
              <input class="bg-white w-full rounded-md py-2 pl-5 pr-3 shadow-sm focus:outline-none border border-gray-300 focus:border-sky-500 focus:ring-sky-500 focus:ring-1 font-semibold" type="file" name="bukti">
            </div>
          </div>
          <div>
            <label>Foto Kegiatan</label>
            <div>
              <input class="bg-white w-full rounded-md py-2 pl-5 pr-3 shadow-sm focus:outline-none border border-gray-300 focus:border-sky-500 focus:ring-sky-500 focus:ring-1 font-semibold" type="file" name="foto_kegiatan">
            </div>
          </div>
          <div>
            <label>Tim Individu</label>
            <div>
              <select v-model="status" class="bg-white w-full rounded-md py-2 pl-5 pr-3 shadow-sm focus:outline-none border border-gray-300 focus:border-sky-500 focus:ring-sky-500 focus:ring-1 font-semibold" name="tim_individu">
                <option value="tim">Tim</option>
                <option selected value="individu">Individu</option>
              </select>
            </div>
          </div>
          <div>
            <label>Anggota Tim</label>
            <div class="rounded-md py-4 bg-white">
              <table class="table-auto w-full">
                <thead class="border-b border-gray-300 rounded-xl">
                <tr>
                  <th>NIM</th>
                  <th>Nama</th>
                  <th class="w-9">Aksi</th>
                </tr>
                </thead>
                <tbody>
                <tr v-for="(item, index) in this.$store.state.mahasiswa" v-bind:key="index">
                  <td>
                    <input @keyup.enter="insertNim(index, item.nim)" class="bg-gray-100 focus:bg-white w-full py-2 pl-5 pr-3 focus:outline-none focus:border-sky-500 focus:ring-sky-500 focus:ring-1 font-semibold" type="text" name="tim_individu" v-model="item.nim">
                  </td>
                  <td>
                    <input disabled class="bg-gray-100 focus:bg-white w-full py-2 pl-5 pr-3 focus:outline-none focus:border-sky-500 focus:ring-sky-500 focus:ring-1 font-semibold" type="text" name="tim_individu" v-model="item.nama">
                  </td>
                  <td class="px-1">
                    <button @click="deleteMahasiswa(index)" class="bg-rose-500 transform focus:scale-110 transition duration-200 text-white text-center rounded-md shadow-md focus:shadow-lg px-1.5"><font-awesome-icon icon="fas fa-minus" /></button>
                  </td>
                </tr>
                <tr>
                  <td>
<!--                    <input class="bg-gray-100 focus:bg-white w-full py-2 pl-5 pr-3 focus:outline-none focus:border-sky-500 focus:ring-sky-500 focus:ring-1 font-semibold" type="text" name="tim_individu">-->
                  </td>
                  <td>
<!--                    <input class="bg-gray-100 focus:bg-white w-full py-2 pl-5 pr-3 focus:outline-none focus:border-sky-500 focus:ring-sky-500 focus:ring-1 font-semibold" type="text" name="tim_individu">-->
                  </td>
                  <td class="px-1">
                    <button @click="addMahasiswa" class="bg-emerald-500 transform focus:scale-110 transition duration-200 text-white text-center rounded-md shadow-md focus:shadow-lg px-1.5"><font-awesome-icon icon="fas fa-plus" /></button>
                  </td>
                </tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>
      </MacCardComponent>
    </div>
  </div>
</template>

<script>
import MacCardComponent from "@/components/widget/MacCardComponent";
export default {
  name: "PenghargaanPage",
  data() {
    return {
      status: null
    }
  },
  components: {
    MacCardComponent
  },
  methods: {
    addMahasiswa: function () {
      this.$store.commit('pushMahasiswa', {nim: null, nama: null})
    },
    insertNim: function (key, nim) {
      this.$store.state.mahasiswa[key].nama = nim
    },
    deleteMahasiswa: function (key) {
      this.$store.commit('deleteMahasiswa', key)
    }
  }
}
</script>

<style scoped>

</style>