<template>
    <v-container>
      <v-card>
        <v-card-title>{{ post.title }}</v-card-title>
        <v-card-subtitle>{{ post.created_at }}</v-card-subtitle>
        <v-card-text>{{ post.content }}</v-card-text>
      </v-card>
    </v-container>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        post: {},
      };
    },
    created() {
      this.fetchPost();
    },
    methods: {
      async fetchPost() {
        try {
          const postId = this.$route.params.id;
          const response = await axios.get(`/api/posts/${postId}/`);
          this.post = response.data;
        } catch (error) {
          console.error('Error fetching post:', error);
        }
      },
    },
  };
  </script>
  