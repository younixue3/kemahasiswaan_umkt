<template>
  <div class="py-0.5 rounded-xl overflow-x-hidden truncate" :class="dropactive ? 'h-full' : 'h-9'">
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
            <ul class="bg-gray-300 text-sm rounded-lg my-2 overflow-hidden truncate transition-all ease-in-out" :class="dropactive ? 'h-full' : 'h-0'">
              <div class="grid grid-cols-1 gap-2 p-0.5">
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
  props: ['height'],
  methods: {
    dropdownactive: function () {
            this.dropactive = !this.dropactive;
        }
  }
}
</script>

<style scoped>

</style>