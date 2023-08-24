<template>
  <div id="app">
    <header>
      <h1>Zeanvas Blog</h1>
    </header>
    <main>
      <PostList />
    </main>
  </div>
</template>

<script>
import PostList from './components/PostList.vue';
import PostDetail from './components/PostDetail.vue';

export default {
  name: 'App',
  components: {
    PostList,
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

header {
  background-color: #35495e;
  color: white;
  padding: 10px;
}

h1 {
  margin: 0;
}

main {
  padding: 20px;
}
</style>
