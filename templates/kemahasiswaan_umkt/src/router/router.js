import Vue from 'vue'
import VueRouter from 'vue-router'
import DashboardLayout from "@/views/layout/DashboardLayout";
import DashboardPage from "@/views/dashboard/DashboardPage";
import PenghargaanPage from "@/views/dashboard/prestasi/PenghargaanPage";
import WorkshopPage from "@/views/dashboard/prestasi/WorkshopPage";
import OrganisasiPage from "@/views/dashboard/prestasi/OrganisasiPage";

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
        component: PenghargaanPage,
      },
        {
        path: 'prestasi-seminar',
        component: WorkshopPage,
      },
        {
        path: 'prestasi-organisasi',
        component: OrganisasiPage,
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