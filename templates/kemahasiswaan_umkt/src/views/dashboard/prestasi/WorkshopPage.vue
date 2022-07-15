<template>
  <div>
    <div class="grid grid-cols-12 gap-x-5 gap-y-5 my-5">
      <MacCardComponent cardsname="Staff | Status" class="col-span-12 overflow-hidden">
        <div class="grid grid-cols-2 gap-5 px-5">
          <div class="col-span-2">
            <label>Event</label>
            <div>
              <input
                  class="bg-white w-full rounded-md py-2 pl-5 pr-3 shadow-sm focus:outline-none border border-gray-300 focus:border-sky-500 focus:ring-sky-500 focus:ring-1 font-semibold"
                  type="text" name="nama_event" v-model="nama_event">
            </div>
          </div>
          <div class="col-span-2">
            <label>URL Kegiatan</label>
            <div>
              <input
                  class="bg-white w-full rounded-md py-2 pl-5 pr-3 shadow-sm focus:outline-none border border-gray-300 focus:border-sky-500 focus:ring-sky-500 focus:ring-1 font-semibold"
                  type="text" name="url_kegiatan" v-model="url_kegiatan">
            </div>
          </div>
          <div class="col-span-2">
            <label>Peyelenggara</label>
            <div>
              <input
                  class="bg-white w-full rounded-md py-2 pl-5 pr-3 shadow-sm focus:outline-none border border-gray-300 focus:border-sky-500 focus:ring-sky-500 focus:ring-1 font-semibold"
                  type="text" name="penyelenggara" v-model="peyelenggara">
            </div>
          </div>
          <div>
            <label>Lingkup/Tingkat</label>
            <div>
              <input
                  class="bg-white w-full rounded-md py-2 pl-5 pr-3 shadow-sm focus:outline-none border border-gray-300 focus:border-sky-500 focus:ring-sky-500 focus:ring-1 font-semibold"
                  type="text" name="lingkup_tingkat" v-model="lingkup_tingkat">
            </div>
          </div>
          <div>
            <label>Jumlah Negara Peserta</label>
            <div>
              <input
                  class="bg-white w-full rounded-md py-2 pl-5 pr-3 shadow-sm focus:outline-none border border-gray-300 focus:border-sky-500 focus:ring-sky-500 focus:ring-1 font-semibold"
                  type="number" name="jumlah_negara" v-model="jumlah_negara">
            </div>
          </div>
          <div class="col-span-2">
            <label>Kategori</label>
            <div>
              <input
                  class="bg-white w-full rounded-md py-2 pl-5 pr-3 shadow-sm focus:outline-none border border-gray-300 focus:border-sky-500 focus:ring-sky-500 focus:ring-1 font-semibold"
                  type="text" name="kategori" v-model="kategori">
            </div>
          </div>
          <div>
            <label>Prestasi yang diraih</label>
            <div>
              <input
                  class="bg-white w-full rounded-md py-2 pl-5 pr-3 shadow-sm focus:outline-none border border-gray-300 focus:border-sky-500 focus:ring-sky-500 focus:ring-1 font-semibold"
                  type="text" name="prestasi_diraih" v-model="prestasi_diraih">
            </div>
          </div>
          <div>
            <label>Ekuivalensi</label>
            <div>
              <input
                  class="bg-white w-full rounded-md py-2 pl-5 pr-3 shadow-sm focus:outline-none border border-gray-300 focus:border-sky-500 focus:ring-sky-500 focus:ring-1 font-semibold"
                  type="text" name="ekuivalensi" v-model="ekuivalensi">
            </div>
          </div>
          <div class="col-span-2">
            <label>Tempat</label>
            <div>
              <input
                  class="bg-white w-full rounded-md py-2 pl-5 pr-3 shadow-sm focus:outline-none border border-gray-300 focus:border-sky-500 focus:ring-sky-500 focus:ring-1 font-semibold"
                  type="text" name="tempat" v-model="tempat">
            </div>
          </div>
          <div>
            <label>Tanggal Mulai</label>
            <div>
              <input
                  class="bg-white w-full rounded-md py-2 pl-5 pr-3 shadow-sm focus:outline-none border border-gray-300 focus:border-sky-500 focus:ring-sky-500 focus:ring-1 font-semibold"
                  type="date" name="tanggal_mulai" v-model="tanggal_mulai">
            </div>
          </div>
          <div>
            <label>Tanggal Selesai</label>
            <div>
              <input
                  class="bg-white w-full rounded-md py-2 pl-5 pr-3 shadow-sm focus:outline-none border border-gray-300 focus:border-sky-500 focus:ring-sky-500 focus:ring-1 font-semibold"
                  type="date" name="tanggal_selesai" v-model="tanggal_selesai">
            </div>
          </div>
          <div class="col-span-2">
            <label>Deskripsi</label>
            <div>
              <textarea v-model="deskripsi"
                  class="bg-white w-full rounded-md py-2 pl-5 pr-3 shadow-sm focus:outline-none border border-gray-300 focus:border-sky-500 focus:ring-sky-500 focus:ring-1 font-semibold"
                  name="deskripsi"></textarea>
            </div>
          </div>
          <div>
            <label>Bukti</label>
            <div>
              <input
                  class="bg-white w-full rounded-md py-2 pl-5 pr-3 shadow-sm focus:outline-none border border-gray-300 focus:border-sky-500 focus:ring-sky-500 focus:ring-1 font-semibold"
                  type="file" name="bukti" @change="insertBukti">
            </div>
          </div>
          <div>
            <label>Foto Kegiatan</label>
            <div>
              <input
                  class="bg-white w-full rounded-md py-2 pl-5 pr-3 shadow-sm focus:outline-none border border-gray-300 focus:border-sky-500 focus:ring-sky-500 focus:ring-1 font-semibold"
                  type="file" name="foto_kegiatan" @change="insertFotoKegiatan">
            </div>
          </div>
          <div>
            <label>Tim Individu</label>
            <div>
              <select v-model="tim_individu"
                      class="bg-white w-full rounded-md py-2 pl-5 pr-3 shadow-sm focus:outline-none border border-gray-300 focus:border-sky-500 focus:ring-sky-500 focus:ring-1 font-semibold">
                <option value="tim">Tim</option>
                <option value="individu" selected>Individu</option>
              </select>
            </div>
          </div>
          <div v-if="tim_individu === 'tim'">
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
                    <input @keyup.enter="insertNim(index, item.nim)"
                           class="bg-gray-100 focus:bg-white w-full py-2 pl-5 pr-3 focus:outline-none focus:border-sky-500 focus:ring-sky-500 focus:ring-1 font-semibold"
                           type="text" v-model="item.nim">
                  </td>
                  <td>
                    <input disabled
                           class="bg-gray-100 focus:bg-white w-full py-2 pl-5 pr-3 focus:outline-none focus:border-sky-500 focus:ring-sky-500 focus:ring-1 font-semibold"
                           type="text" v-model="item.nama">
                  </td>
                  <td class="px-1">
                    <button @click="deleteMahasiswa(index)"
                            class="bg-rose-500 transform focus:scale-110 transition duration-200 text-white text-center rounded-md shadow-md focus:shadow-lg px-1.5">
                      <font-awesome-icon icon="fas fa-minus"/>
                    </button>
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
                    <button @click="addMahasiswa"
                            class="bg-emerald-500 transform focus:scale-110 transition duration-200 text-white text-center rounded-md shadow-md focus:shadow-lg px-1.5">
                      <font-awesome-icon icon="fas fa-plus"/>
                    </button>
                  </td>
                </tr>
                </tbody>
              </table>
            </div>
          </div>
          <div v-if="tim_individu === 'individu'">
            <label>Mahasiswa</label>
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
                    <input @keyup.enter="insertNim(index, item.nim)"
                           class="bg-gray-100 focus:bg-white w-full py-2 pl-5 pr-3 focus:outline-none focus:border-sky-500 focus:ring-sky-500 focus:ring-1 font-semibold"
                           type="text" v-model="item.nim">
                  </td>
                  <td>
                    <input disabled
                           class="bg-gray-100 focus:bg-white w-full py-2 pl-5 pr-3 focus:outline-none focus:border-sky-500 focus:ring-sky-500 focus:ring-1 font-semibold"
                           type="text" v-model="item.nama">
                  </td>
                  <td class="px-1">
                    <button @click="deleteMahasiswa(index)"
                            class="bg-rose-500 transform focus:scale-110 transition duration-200 text-white text-center rounded-md shadow-md focus:shadow-lg px-1.5">
                      <font-awesome-icon icon="fas fa-minus"/>
                    </button>
                  </td>
                </tr>
                </tbody>
              </table>
            </div>
          </div>
          <div class="col-span-2">
            <button @click="submitForm"
                    class="bg-emerald-500 transform focus:scale-110 transition duration-200 text-white text-center rounded-md shadow-md focus:shadow-lg px-1.5">
              Insert
            </button>
            <button @click="cancelForm"
                    class="bg-emerald-500 transform focus:scale-110 transition duration-200 text-white text-center rounded-md shadow-md focus:shadow-lg px-1.5">
              Cancel
            </button>
          </div>
        </div>
      </MacCardComponent>
    </div>
  </div>
</template>

<script>
import MacCardComponent from "@/components/widget/MacCardComponent";
import axios from "axios";

export default {
  name: "WorkshopPage",
  data() {
    return {
      foto_kegiatan: {},
      bukti: null,
      nama_event : null,
      url_kegiatan : null,
      penyelenggara : null,
      lingkup_tingkat : null,
      jumlah_negara : null,
      kategori : null,
      prestasi_diraih : null,
      ekuivalensi : null,
      tempat : null,
      tanggal_mulai : null,
      tanggal_selesai : null,
      deskripsi : null,
      tim_individu : 'individu',
      anggota: []
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
      for (let i in this.$store.state.mahasiswa) {
        if (nim === this.$store.state.mahasiswa[i].nim) {
          if (key == i) {
            axios.post(process.env.VUE_APP_BASE_URL + "/api/insert-nim/", {
            nim: nim
            })
            .then(resp => {
              console.log(resp)
              this.$store.state.mahasiswa[key].nama = resp.data.name
              this.anggota.push(nim)
            })
            .catch(e => {
              console.log(e)
              this.$store.state.mahasiswa[key].nama = null
            })
          } else {
            alert('anda sudah memasukkan NIM tersebut')
          break
          }
        }
      }
    },
    deleteMahasiswa: function (key) {
      if (key != 0) {
        this.$store.commit('deleteMahasiswa', key)
      }
    },
    submitForm: function () {
      const formData = new FormData()
      formData.append('foto_kegiatan', this.foto_kegiatan, this.foto_kegiatan.name)
      formData.append('bukti', this.bukti, this.bukti.name)
      formData.append('nama_event', this.nama_event)
      formData.append('url_kegiatan', this.url_kegiatan)
      formData.append('penyelenggara', this.penyelenggara)
      formData.append('lingkup_tingkat', this.lingkup_tingkat)
      formData.append('jumlah_negara', this.jumlah_negara)
      formData.append('kategori', this.kategori)
      formData.append('prestasi_diraih', this.prestasi_diraih)
      formData.append('ekuivalensi', this.ekuivalensi)
      formData.append('tempat', this.tempat)
      formData.append('tanggal_mulai', this.tanggal_mulai)
      formData.append('tanggal_selesai', this.tanggal_selesai)
      formData.append('deskripsi', this.deskripsi)
      formData.append('tim_individu', this.tim_individu)
      formData.append('token', this.$store.state.auth.token)
      formData.append('anggota', JSON.stringify(this.anggota))
      formData.append('jenis_prestasi', 'organisasi')
      axios.post(process.env.VUE_APP_BASE_URL + "/prestasi/insert-prestasi", {formData}, {
      })
      .then(resp => {
        console.log(resp)
      })
      .catch(e => console.log(e))
    },
    insertFotoKegiatan: function () {
      this.foto_kegiatan = event.target.files[0]
    },
    insertBukti: function () {
      this.bukti = event.target.files[0]
    },
    cancelForm: function () {
      this.nama_event = null
      this.url_kegiatan = null
      this.penyelenggara = null
      this.lingkup_tingkat = null
      this.jumlah_negara = null
      this.kategori = null
      this.prestasi_diraih = null
      this.ekuivalensi = null
      this.tempat = null
      this.tanggal_mulai = null
      this.tanggal_selesai = null
      this.deskripsi = null
      this.tim_individu = null
    }
  }
}
</script>

<style scoped>

</style>