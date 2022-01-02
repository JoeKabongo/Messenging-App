<template>
  <div id="conversation-container">
    <div
      class="conversation-item"
      v-for="item in lastConversations"
      :key="item"
    >
      <img
        class="profile-picture"
        src="../assets/profilePicture.png"
        alt="profile picture"
      />
      <span>
        {{ item }}
      </span>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Conversations',
  data() {
    return {
      lastConversations: ['Jonathan x', 'maxin1721', 'steph', 'maggi1234'],
    }
  },
}
</script>

<style scoped>
#conversation-container {
  position: absolute;
  top: 0;
  bottom: 0;
  width: 400px;
  background: red;
}
.conversation-item {
  display: flex;
  align-items: center;
  padding: 10px;
}
.profile-picture {
  width: 50px;
}
</style>
