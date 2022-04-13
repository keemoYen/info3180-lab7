<template>
    <form @submit.prevent="uploadPhoto" method="post" action="/api/upload">
        <label for="description">Description</label>
        <textarea name="description" rows="4" cols="50"></textarea>
    </form>
</template>

<script>

fetch("/api/upload",{
    method: 'POST'
}).then(function(response){
    return response.json();
}).then(function (data){
    //display a sucess message
    console.log(data);
}).catch(function(error){
    console.log(error);
});
</script>

<style scoped>

</style>
