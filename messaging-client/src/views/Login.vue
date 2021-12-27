<template>
<div class="container">
    <h2>Login and chat with your favorite people</h2>
    <form @submit.prevent="onSubmit" class="login-form">
        <input 
            type="email" 
            name="email" 
            placeholder="Enter email address" 
            v-model="email" />

        <input 
            type="password" 
            placeholder="Enter password" 
            v-model="password"/>
        <div class="btn-block">
           <button type="submit" class="btn"> Login </button> 
        </div>
    </form>

     <div>
        Dont have an account yet? <router-link to="/signup">Signup here</router-link>
    </div>

</div>

    
</template>

<script>
export default {
    name: 'Login',
    data() {
        return {
            email: '',
            password: '',
        }
    },
    methods: {
        onSubmit() {
            console.log(this.email);
            console.log(this.password);
        }
    }
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
    border: 1px solid rgba(0, 0, 0, .20);
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