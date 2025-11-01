<script>

    let {item} = $props()

</script>


<div class="actor-card">
    <img class="actor-profile" src="{item.profile_pic_url}" alt={item.name} />
    <div class="actor-details">
        <p class="actor-name">{item.name}</p>
        <p class="actor-popularity">Popularidade: {item.popularity}</p>
        <p class="actor-department">Departamento: {item.known_for_department}</p>
    </div>
</div>

<style>
    .actor-card {
    display: flex;
    background-color: #fff;
    border-radius: 10px;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
    padding: 20px;
    margin: 20px;
    max-width: 500px;
    transition: transform 0.3s ease;
    overflow: hidden;
}

.actor-card:hover {
    transform: translateY(-5px);
}

.actor-profile {
    width: 120px;
    height: 180px;
    object-fit: cover;
    border-radius: 10px;
    margin-right: 20px;
}

.actor-details {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
}

.actor-name {
    font-size: 1.5em;
    font-weight: bold;
    color: #333;
    margin: 0;
}

.actor-popularity,
.actor-department {
    font-size: 1em;
    color: #555;
    margin-top: 10px;
}

</style>