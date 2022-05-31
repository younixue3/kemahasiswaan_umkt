<template>
  <div>
    <div class="absolute bg-white shadow-lg border border-gray-300 rounded-xl w-72 md:w-96 left-1/2 top-1/2 transform -translate-x-1/2 -translate-y-1/2 text-center">
        <div class="my-10">
            <div class="text-4xl font-bold">Welcome</div>
            <div class="text-lg font-light leading-3">Sign in to your account</div>
        </div>
        <div class="mx-5 my-10">
            <input type="text" class="flex-1 block w-full rounded-t-xl focus:outline-none px-3 py-1.5 border border-b-0 border-gray-300" placeholder="Username" name="username" v-model="username">
            <input type="password" class="flex-1 block w-full rounded-b-xl focus:outline-none px-3 py-1.5 border border-gray-300" placeholder="Password" name="password" v-model="password">
        </div>
        <div class="mx-5 my-10">
            <div class="m-auto flex space-x-5">
                <button class="bg-indigo-500 text-xl text-white text-center rounded-md shadow-md w-full px-5 py-1"><span class="align-text-top">Sign in</span></button>
                <button class="text-xl text-indigo-500 text-center rounded-md shadow-md border border-gray-100 w-full px-5 py-1"><span class="align-text-top">Sign up</span></button>
            </div>
        </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "LoginPage",
  methods: {
    login() {
      console.log(process.env.VUE_APP_BASE_URL + "/api/auth")
      axios.post(process.env.VUE_APP_BASE_URL + "/api/auth", {
        username: this.username,
        password: this.password
      })
      .then(resp => {
        this.$store.commit('auth', resp.data)
      })
      .catch(e => {
        console.log(e)
      })
      .finally(() => {
        if (this.$store.state.auth.token !== null) {
          this.notifikasi.active = false
          this.notifikasi.massage = null
          this.$router.push({name: 'login', query: {redirect: '/path'}})
        } else {
          console.log('Akun atau Password Salah')
          this.$store.state.notification.active = true
          this.notifikasi.massage = 'Akun atau Password Salah'
        }
      })
    },

  }
}
</script>

<style scoped>

</style>