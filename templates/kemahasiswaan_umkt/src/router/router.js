import Vue from 'vue'
import VueRouter from 'vue-router'
import DashboardLayout from "@/views/layout/DashboardLayout";
import DashboardPage from "@/views/dashboard/DashboardPage";

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'dashboard',
    component: DashboardLayout,
    children: [
      {
        path: '',
        component: DashboardPage,
      },
        {
        path: 'prestasi-penghargaan',
        component: DashboardPage,
      },
        {
        path: 'prestasi-seminar',
        component: DashboardPage,
      },
      // {
      //   path: '/form',
      //   component: FormPage,
      //   meta: { requiresAuth: true },
      // },
      // {
      //   path: '/approval',
      //   component: SearchPage,
      //   meta: { requiresAuth: true },
      // },
    ]
  },
]

const router = new VueRouter({
  routes,
  linkActiveClass: 'is-active'
})

// router.beforeEach((to, from, next) => {
//   if (to.matched.some(record => record.meta.requiresAuth)) {
//     if (store.state.auth.status) {
//       next()
//     } else {
//       next({
//         path: '/login',
//         query: { redirect: to.fullPath }
//       })
//     }
//   } else {
//     if (store.state.auth.status) {
//       next({
//         path: '/',
//         query: { redirect: to.fullPath }
//       })
//     } else {
//       next()
//     }
//   }
// })

export default router