<template>
  <div class="container">
    <h2>Login and chat with your favorite people</h2>
    <form @submit.prevent="onSubmit" class="login-form">
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
      <div class="btn-block">
        <button type="submit" class="btn">Login</button>
      </div>
    </form>

    <div>
      Dont have an account yet?
      <router-link to="/signup">Signup here</router-link>
    </div>
  </div>
</template>

<script>
import axios from '../axios'

export default {
  name: 'Login',
  data() {
    return {
      email: '',
      password: '',
    }
  },
  methods: {
    async onSubmit() {
      if (this.email !== '' || this.password !== '') {
        alert('A field cannot be empty')
        return
      }
      //TODO: save user information after i implement login on backend
      try {
        const response = await axios.post('/login', {
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
  width: 100%;
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
