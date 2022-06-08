<template>
  <div id="mobile-menu"
       class="h-full md:h-auto text-gray-800 z-40 fixed duration-300 bg-gray-100 shadow-md md:static"
       @mouseenter="CollapsedHover()" @mouseleave="CollapsedHover()"
       :class="collapsed ? 'w-60 md:w-80 lg:w-80' : 'w-0 md:w-11 lg:w-11 md:hover:w-44'">
    <div class="font-bold text-xl h-16 pr-2 md:pr-0 flex relative z-50">
      <div class="flex transition-all ease-in-out duration-500" :class="collapsed ? 'w-full' : 'w-0'">
        <img class="min-h-5 h-5 mx-3 my-auto" src="" alt="">
        <a
            class="my-auto text-2xl align-middle overflow-hidden truncate font-light">
          Dashboard
        </a>
      </div>
      <button @click="CloseBar()" type="button"
              class="transition-all bg-gray-700 shrink-0 -mr-3 w-10 h-10 text-white rounded-lg ease-in-out duration-500 z-50 m-auto -mr-5">
        <!-- Heroicon name: outline/x -->
        <font-awesome-icon :icon="collapsed ? 'fas fa-bars' : 'fas fa-times'"/>
      </button>
    </div>
    <div class="text-lg font-normal tracking-tight">
      <div class="py-5 px-1 py-2 grid grid-cols-1">
        <NavbarDropdownComponent height="h-[7.3rem]">
          <template #group-icon>
            <font-awesome-icon icon="fas fa-graduation-cap"/>
          </template>
          <template #group>
            <div>Prestasi Mahasiswa</div>
          </template>
          <template #item>
            <router-link to="/prestasi-penghargaan" class="px-2 rounded-md overflow-hidden">
              <button class="my-1 cursor-pointer flex w-52">
                <div class="mr-2">
                  <font-awesome-icon icon="fas fa-medal"/>
                </div>
                <span class="">Penghargaan</span>
              </button>
            </router-link>
            <router-link to="/prestasi-seminar" class="px-2 rounded-md overflow-hidden">
              <button class="my-1 cursor-pointer flex w-52">
                <div class="mr-2">
                  <font-awesome-icon icon="fas fa-chalkboard-teacher"/>
                </div>
                <span>Seminar/Workshop/Keahlian</span></button>
            </router-link>
            <router-link to="/prestasi-organisasi" class="px-2 rounded-md overflow-hidden">
              <button class="my-1 cursor-pointer flex w-52">
                <div class="mr-2">
                  <font-awesome-icon icon="fas fa-sitemap"/>
                </div>
                <span>Organisasi/Kepanitiaan</span></button>
            </router-link>
          </template>
        </NavbarDropdownComponent>
        <div @click="logout" class="py-0.5 rounded-xl overflow-hidden truncate cursor-pointer">
          <div class="hover:bg-gray-200 px-2 pt-1 rounded-lg">
            <div class="flex w-52">
              <div class="w-1/6">
                <font-awesome-icon icon="fas fa-sign-out"/>
              </div>
              <span>Logout</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import NavbarDropdownComponent from "@/components/layout/widget/NavbarDropdownComponent";
// import axios from "axios";

export default {
  name: "NavbarDashComponent",
  components: {
    NavbarDropdownComponent
  },
  data() {
    return {
      collapsed: true,
      hover: true
    }
  },
  methods: {
    CloseBar: function () {
      if (this.collapsed === true) {
        this.hover = false
        this.collapsed = false
      } else {
        this.hover = true
        this.collapsed = true
      }
    },
    CollapsedHover: function () {
      if (this.hover === true) {
        return 'nothing';
      } else {
        this.collapsed = false;
      }
    },
    logout: function () {
      window.location.href = 'https://sso.umkt.ac.id/cas/logout?service=http://127.0.0.1:8080/login'
      // axios.post(process.env.VUE_APP_BASE_URL + '/api/auth/logout/')
      //     .then(resp => {
      //       console.log(resp)
      //       // this.$store.commit('auth', resp.data)
      //       // this.$router.push({ path: '/' })
      //     })
      //     .catch(e => console.log(e))
      // this.$store.commit('authLogout')
      // this.$router.push({ name: 'login', query: { redirect: '/login' } });
    }
  }
}
</script>

<style scoped>

</style>