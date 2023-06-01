import { Text, View, FlatList } from 'react-native';
import { useEffect, useState } from 'react';
import axios from 'axios';

const twitterApi = axios.create({
    baseURL: 'http://localhost:5000/twitter/',
    proxy: false
})

const HomeScreen = () => {
    const [tweets, setTweets] = useState([]);
    useEffect(() => {
        async function getTweets() {
            let response = await twitterApi.get('/tweets');
            console.log(response.data);
            setTweets(response.data);
        }
        getTweets();
    }, []);

    return (
        <View>
            <FlatList
                data={tweets}
                keyExtractor={(item) => { item.id }}
                renderItem={({ item }) => {
                    return (<View>
                        <Image
                            source={item.image}
                        />
                        <Text>{item.text}</Text>
                    </View>);
                }}
            />
        </View>
    );
}

export default HomeScreen;