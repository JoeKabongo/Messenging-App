<template>
  <div>
    <MessagesNavigation />
    <Messages />
  </div>
</template>

<script>
import MessagesNavigation from '../components/MessagesNavigation.vue'
import Messages from '../components/Messages.vue'
export default {
  name: 'Home',
  components: {
    MessagesNavigation,
    Messages,
  },
  methods: {
    logout() {
      localStorage.removeItem('token')
      this.$router.push('/login')
    },
  },
}
</script>

<style scoped></style>
