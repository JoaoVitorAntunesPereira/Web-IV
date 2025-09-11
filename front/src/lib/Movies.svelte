<script>

    let results = $state(null);
    async function getMovies() {
        let endpoint = `http://localhost:8000/movies/top`;
        const res = await fetch(endpoint);
        const data = await res.json();
        if (res.ok) {
            return data;
        } else {throw new Error(data); }
    }

    function handleClick() {
    getMovies().then((data)=>{
        results = data;
    });
    }

</script>

<h2>Componente</h2>

<button
    onclick={()=>handleClick()}
>top rated
</button>

<div class="results">
   {#if results}
       {#each results as item}
       <p>{item.title}</p>
       <img src={item.poster_url} alt="poster">
       {/each}
   {/if}
</div>

