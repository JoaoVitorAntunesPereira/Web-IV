<script>
    import { onMount } from "svelte";
    import PersonCard from "$lib/PersonCard.svelte";

    let results = $state(null)

    async function getFavorites() {

        let endpoint = `http://localhost:8000/person/favorites`
        
        const res = await fetch(endpoint)
        const data = await res.json()

        if(res.ok){
            return data
        }else{
            throw new Error(data)
        }

    }

    getFavorites().then((data) => {
        results = data
    })

    onMount(() => {
        getFavorites()
    })

</script>

<div class="results">
    {#if results}
        {#each results as item}
            <PersonCard {item}/>
        {/each}
    {/if}
</div>
