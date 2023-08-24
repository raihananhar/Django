import Vue from 'vue';
import VueRouter from 'vue-router';
import PostList from '../components/PostList.vue';
import PostDetail from '../components/PostDetail.vue';

Vue.use(VueRouter);

const routes = [
  { path: '/', component: PostList },
  { path: '/post/:id', name: 'post-detail', component: PostDetail },
];

const router = new VueRouter({
  routes,
});

export default router;
