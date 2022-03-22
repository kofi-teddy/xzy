import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/incident/:id",
    name: "IncidentDetail",
    component: IncidentDetail,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
