<script>
    import { onMount } from "svelte";
    import MovieCard from "$lib/MovieCard.svelte";

    let results = $state(null);

    async function getMovies() {
        let endpoint = `http://localhost:8000/movies/top/1`;
        const res = await fetch(endpoint);
        const data = await res.json();
        if (res.ok) {
            return data;
        } else {throw new Error(data); }
    }

    getMovies().then((data)=>{
            results = data;
    });

    onMount(() => {
        getMovies()
    }) 

</script> 

<h2>Componente</h2>

<div class="results">
   {#if results}
       {#each results as item}
            <MovieCard {item}/>
       {/each}
   {/if}
</div>

