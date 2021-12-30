<template>
  <div>
    <h1>Home</h1>
    <button @click="logout">Logout</button>
  </div>
</template>

<script>
export default {
  name: 'Home',
  methods: {
    logout() {
      localStorage.removeItem('token')
      this.$router.push('/login')
    },
  },
}
</script>
