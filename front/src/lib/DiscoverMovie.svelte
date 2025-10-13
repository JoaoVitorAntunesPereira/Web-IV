<script>
    import { onMount } from "svelte";
    import MovieCard from "./MovieCard.svelte";

    let results = $state(null)
    let year = '2025'
    let popularity = 'asc'

    async function getDiscoverMovie() {
        let endpoint = `http://localhost:8000/discover/movie?release_year=${year}&popularity=${popularity}`

        console.log(endpoint)
        
        const res = await fetch(endpoint)
        const data = await res.json()
        results = data

        if(res.ok){
            return data
        }else{
            throw new Error(data)
        }
    }

    getDiscoverMovie().then((data)=>{
        console.log("resultados",results)
    });
    

	async function handleSubmit(event) {
		event.preventDefault()
		await getDiscoverMovie()
	}


</script>

<h2>Form</h2>

<p>{year}</p>
<p>{popularity}</p>

<form action="get" on:submit|preventDefault={handleSubmit}>
    <label for="year">Release year</label>
    <input id="year" type="text" bind:value={year}>

    <fieldset>
        <legend>Popularity</legend>

        <input type="radio" bind:group={popularity} value="asc" checked name="popularity" on:change|preventDefault={handleSubmit}/>
        <label for="popularity">Ascent</label>

        <input type="radio" bind:group={popularity} value="desc" name="popularity" on:change|preventDefault={handleSubmit}/>
        <label for="popularity">Descent</label>
    </fieldset>

    <button type="submit">Buscar</button>

</form>

{#if results}
	<h3>Resultados</h3>
	{#each results as item}
		<MovieCard {item} />
	{/each}
{/if}