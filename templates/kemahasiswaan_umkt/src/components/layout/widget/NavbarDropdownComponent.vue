<template>
  <div class="py-0.5 my-1 rounded-xl overflow-hidden truncate">
        <div>
            <div class="hover:bg-gray-200 px-2 pt-1 rounded-lg cursor-pointer" @click="dropdownactive">
                <div class="flex w-52">
                    <div class="w-1/6">
                        <slot name="group-icon"></slot>
                    </div>
                    <div class="flex-1">
                      <slot name="group"></slot>
                    </div>
                    <span class="overflow-hidden w-8 text-center">
                        <i class="my-auto fas fa-chevron-right transition-all duration-500 transform"></i>
                    </span>
                </div>
            </div>
            <ul class="bg-gray-200 text-sm rounded-lg my-2 overflow-hidden truncate transition-all ease-in-out" :class="dropactive ? 'h-20' : 'h-0'">
              <div class="grid grid-cols-1 gap-2 p-2">
                <slot name="item"></slot>
              </div>
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