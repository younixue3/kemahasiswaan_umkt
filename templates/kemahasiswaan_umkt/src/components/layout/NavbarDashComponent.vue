<template>
  <div id="mobile-menu"
       class="h-full md:h-auto text-gray-800 z-40 fixed duration-300 bg-gray-100 shadow-md md:static"
       @mouseenter="CollapsedHover()" @mouseleave="CollapsedHover()"
       :class="collapsed ? 'w-60 md:w-80 lg:w-80' : 'w-0 md:w-11 lg:w-14 md:hover:w-44'">
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
        <font-awesome-icon :icon="collapsed ? 'fas fa-bars' : 'fas fa-times'" />
      </button>
    </div>
    <div class="text-lg font-normal tracking-tight">
      <div class="py-5 px-1 py-2">
        <NavbarDropdownComponent height="h-[7.3rem]">
          <template #group-icon>
            <font-awesome-icon icon="fas fa-graduation-cap" />
          </template>
          <template #group>
            <div>Prestasi Mahasiswa</div>
          </template>
          <template #item>
            <router-link to="/prestasi-penghargaan" class="px-2 rounded-md overflow-hidden">
              <button class="my-1 cursor-pointer flex w-52">
                <div class="mr-1.5">
                  <font-awesome-icon icon="fas fa-medal" />
                </div>
                <span class="">Penghargaan</span>
              </button>
            </router-link>
            <router-link to="/prestasi-seminar" class="px-2 rounded-md overflow-hidden">
              <button class="my-1 cursor-pointer flex w-52">
                 <div class="mr-1.5">
                  <font-awesome-icon icon="fas fa-chalkboard-teacher" />
                </div>
                <span>Seminar/Workshop/Keahlian</span></button>
            </router-link>
            <router-link to="/prestasi-organisasi" class="px-2 rounded-md overflow-hidden">
              <button class="my-1 cursor-pointer flex w-52">
                 <div class="mr-1.5">
                  <font-awesome-icon icon="fas fa-sitemap" />
                </div>
                <span>Organisasi/Kepanitiaan</span></button>
            </router-link>
          </template>
        </NavbarDropdownComponent>
      </div>
    </div>
  </div>
</template>

<script>
import NavbarDropdownComponent from "@/components/layout/widget/NavbarDropdownComponent";

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
  }
}
</script>

<style scoped>

</style>