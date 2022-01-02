<template>
  <div>
    <h1>Home</h1>
    <Conversations />
    <button @click="logout">Logout</button>
  </div>
</template>

<script>
import Conversations from '../components/Conversations.vue'
export default {
  name: 'Home',
  components: {
    Conversations,
  },
  methods: {
    logout() {
      localStorage.removeItem('token')
      this.$router.push('/login')
    },
  },
}
</script>
