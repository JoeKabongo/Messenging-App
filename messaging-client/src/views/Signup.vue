<template>
  <div class="container">
    <h2>Signup and chat with your favorite people</h2>
    <form @submit.prevent="onSubmit" class="login-form">
      <input
        type="text"
        name="username"
        placeholder="Enter username"
        v-model="username"
        required
      />

      <input
        type="email"
        name="email"
        placeholder="Enter email address"
        v-model="email"
        required
      />

      <input
        type="password"
        placeholder="Enter password"
        v-model="password"
        required
      />

      <input
        type="password"
        placeholder="Confirm password"
        v-model="passwordConfirmation"
        required
      />
      <div class="btn-block">
        <button type="submit" class="btn">Signup</button>
      </div>
    </form>

    <div>
      Already have an account? <router-link to="/login">Login here</router-link>
    </div>
  </div>
</template>

<script>
import axios from '../axios'

export default {
  name: 'Signup',
  data() {
    return {
      username: '',
      email: '',
      password: '',
      passwordConfirmation: '',
    }
  },
  methods: {
    async onSubmit() {
      if (
        this.username === '' ||
        this.email === '' ||
        this.password === '' ||
        this.passwordConfirmation === ''
      ) {
        alert('A field cannot be empty')
        return
      }

      if (this.password !== this.passwordConfirmation) {
        alert('passwords do not match')
        return
      }

      //TODO: save user information after i implement login on backend
      try {
        const response = await axios.post('/signup', {
          username: this.usermame,
          email: this.email,
          password: this.password,
        })
        console.log(response)
        this.router.push('/')
      } catch (error) {
        alert('request not successfull, something went wrong')
      }
    },
  },
}
</script>

<style scope>
.container {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  min-height: 100vh;
}

.login-form {
  width: 300px;
  margin-top: 30px;
}
input {
  width: 100%;
  height: 40px;
  margin-bottom: 20px;
  border-radius: 4px;
  padding: 0 16px;
  font-size: 20px;
  border: 1px solid rgba(0, 0, 0, 0.2);
}

.btn-block {
  width: 100%;
  text-align: center;
  margin-bottom: 20px;
}
.btn {
  color: #fff;
  border-radius: 15px;
  background: #0a7cff;
  padding: 9.5px 20px;
  font-size: 15px;
  border: 0;
}
</style>
