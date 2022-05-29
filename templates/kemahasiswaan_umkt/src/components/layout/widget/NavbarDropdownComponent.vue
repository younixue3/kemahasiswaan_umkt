<template>
  <div class="py-0.5 my-1 rounded-xl overflow-hidden truncate">
        <div>
            <div class="hover:bg-gray-200 px-2 pt-1 rounded-lg cursor-pointer" @click="dropdownactive">
                <div class="flex justify-between w-full">
                    <div class="w-1/6">
                        <i class="fa-solid fa-users mr-3"></i>
                    </div>
                    <div class="flex-1">
                      <slot></slot>
                    </div>
                    <span class="overflow-hidden w-8 text-center">
                        <i class="my-auto fas fa-chevron-right transition-all duration-500 transform"></i>
                    </span>
                </div>
            </div>
            <ul class="bg-gray-200 rounded-lg px-2.5 my-2 h-full truncate">
<!--                  <slot name="item"></slot>-->
                <a>
                    <div onclick="DropDownItem()" class="my-1 cursor-pointer">
                        <div class="ml-1 mr-5 w-2 h-2 inline-block rounded-full ring ring-gray-800 ring-offset-2"></div>
                        <span class="">Alumni</span></div>
                </a>
                <a>
                    <div onclick="DropDownItem()" class="my-1 cursor-pointer">
                        <div class="ml-1 mr-5 w-2 h-2 inline-block rounded-full ring ring-gray-800 ring-offset-2"></div>
                        <span>Orang Tua</span></div>
                </a>
            </ul>
        </div>
    </div>
</template>

<script>
export default {
  name: "NavbarDropdownComponent",
  data() {
      return {
          dropactive: false
      }
  },
  methods: {
    dropdownactive: function () {
            this.dropactive = !this.dropactive;
        }
  }
}
</script>

<style scoped>

</style>