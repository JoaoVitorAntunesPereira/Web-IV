<script>
    let {debug} = $state(false)
    let {item} = $props();

</script>

<div class="item-container">
    <img class="item-poster" src="{item.poster_url}" alt="poster" />
    <div class="item-details">
        <p class="item-title">{item.title}</p>
        <p class="item-popularity">Popularidade: {item.popularity}</p>
        <p class="item-release-date">{item.release_date}</p>
        {#if item.genres_obj}
            <p>Gêneros: 
            {#each item.genres_obj as genre}
                {genre.name}, 
            {/each}
            </p>
        {/if}
    </div>
</div>

<input type="checkbox" bind:checked={debug}>
{#if debug}
<pre>
    {JSON.stringify(item, null, 2)}
</pre>
{/if}

<style>
    .item-container {
    display: flex;
    background-color: #fff;
    border-radius: 10px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    padding: 20px;
    margin: 20px;
    max-width: 500px;
    transition: transform 0.3s ease;
}

.item-container:hover {
    transform: translateY(-5px);
}

.item-poster {
    max-width: 150px;
    border-radius: 10px;
    margin-right: 20px;
}

.item-details {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
}

.item-title {
    font-size: 1.5em;
    font-weight: bold;
    color: #333;
    margin: 0;
}

.item-popularity,
.item-release-date {
    font-size: 1em;
    color: #555;
}

.item-popularity {
    margin-top: 5px;
}

.item-release-date {
    margin-top: 10px;
}

</style>