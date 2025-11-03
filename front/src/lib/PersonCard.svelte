<script>
    import { json } from "@sveltejs/kit";

    let {item} = $props()
    let endpoint
    let isFavorite = $state(false);
    let results
    
    async function toggleFavorite() {
        isFavorite = !isFavorite;


        if(isFavorite){
            console.log(`Item ${item.name} favorito: ${isFavorite}`);
            console.log(JSON.stringify(item))
            
            endpoint = `http://localhost:8000/person/save`
            const res = await fetch(endpoint, {
                method: "POST",
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(item)
            })

            const data = await res.json()
            results = data

            if(res.ok){
                return data
            }else{
                throw new Error(data)
            }

        }else if(!isFavorite){
            endpoint = `http://localhost:8000/person/delete?person_id=${item.id}`
            const res = await fetch(endpoint)
            const data = await res.json()
            results = data

            if(res.ok){
                return data
            }else{
                throw new Error(data)
            }

        }

    }
</script>


<div class="actor-card">
    <button 
        class="favorite-btn" 
        onclick={toggleFavorite} 
        aria-label="Adicionar aos favoritos"
    >
        <svg 
            class="star-icon" 
            class:favorited={isFavorite} 
            xmlns="http://www.w3.org/2000/svg" 
            viewBox="0 0 24 24" 
            fill="none" 
            stroke="currentColor" 
            stroke-width="2" 
            stroke-linecap="round" 
            stroke-linejoin="round"
        >
            <polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon>
        </svg>
    </button>
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
        position: relative; 
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

    .favorite-btn {
        position: absolute;
        top: 15px;
        right: 15px;
        background: none;
        border: none;
        padding: 5px;
        cursor: pointer;
        border-radius: 50%;
        transition: background-color 0.2s;
    }

    .favorite-btn:hover {
        background-color: #f0f0f0;
    }

    .star-icon {
        width: 24px;
        height: 24px;
        stroke: #888;
        stroke-width: 2;
        fill: none;
        transition: fill 0.2s, stroke 0.2s;
    }
    .star-icon.favorited {
        fill: #facc15;
        stroke: #facc15;
    }
</style>