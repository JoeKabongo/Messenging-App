<template>
  <div id="conversation-container">
    <h1>Messages</h1>
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
  name: 'MessagesNavigation',
  data() {
    return {
      lastConversations: ['Jonathan x', 'maxin1721', 'steph', 'maggi1234'],
    }
  },
}
</script>

<style scoped>
#conversation-container {
  position: fixed;
  top: 0;
  display: inline-block;
  width: 300px;
  height: 100vh;
  border-right: 1px solid #ebebeb;
  padding: 5px;
}
.conversation-item {
  display: flex;
  align-items: center;
  padding: 10px;
}

.conversation-item:hover {
  background: #ebebeb;
  cursor: pointer;
}

.profile-picture {
  width: 50px;
}
</style>
