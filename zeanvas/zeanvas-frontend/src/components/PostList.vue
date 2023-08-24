<template>
    <div class="post-list">
      <v-container>
        <h2 class="mb-4">List of Posts</h2>
        <v-card v-for="post in posts" :key="post.id" class="mb-3">
          <v-card-title>
            <router-link :to="{ name: 'post-detail', params: { id: post.id } }">
              {{ post.title }}
            </router-link>
          </v-card-title>
          <v-card-subtitle>{{ post.created_at }}</v-card-subtitle>
          <v-card-text>{{ post.content }}</v-card-text>
        </v-card>
      </v-container>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        posts: [],
      };
    },
    created() {
      this.fetchPosts();
    },
    methods: {
      async fetchPosts() {
        try {
          const response = await axios.get('/api/posts/');
          this.posts = response.data;
        } catch (error) {
          console.error('Error fetching posts:', error);
        }
      },
    },
  };
  </script>
  
  <style scoped>
  .post-list {
    max-width: 800px;
    margin: 0 auto;
    padding: 20px;
  }
  
  /* Styling untuk komponen Vuetify, jika diperlukan */
  </style>
  