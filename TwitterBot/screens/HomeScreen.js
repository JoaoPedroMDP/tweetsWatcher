import { Text, Image, View, FlatList, StyleSheet } from 'react-native';
import { useEffect, useState } from 'react';
import axios from 'axios';

const twitterApi = axios.create({
    baseURL: 'https://joaopedromdp-improved-system-w99pxvjv55p25rgg-5000.preview.app.github.dev/twitter/',
    proxy: false
})

const HomeScreen = () => {
    const [tweets, setTweets] = useState([]);
    useEffect(() => {
        async function getTweets() {
            let response = await twitterApi.get('/tweets');
            setTweets(response.data);
        }
        getTweets();
    }, []);

    return (
        <View style={styles.page}>
            <View style={styles.header}>
                <Text style={styles.title}>Tweete com as hashtags #TADS #feiraUFPR e apareça aqui!!</Text>
            </View>
            <FlatList
                style={styles.container}
                data={tweets}
                numColumns={3}
                keyExtractor={(item) => { return item.id }}
                renderItem={({ item }) => {
                    return (
                        <View style={styles.card}>
                            <Image
                                style={styles.image}
                                source={item.image}
                            />
                            <Text style={styles.name}>{item.name}</Text>
                            <Text>{item.text}</Text>
                        </View>);
                }}
            />
        </View>
    );
}

const styles = StyleSheet.create({
    card: {
        margin: "10px",
        elevation: "5px",
        borderRadius: "5px",
        width: "30vw"
    },
    name: {
        fontWeight: "bold"
    },
    image: {
        height: "75px",
        width: "75px",
        borderRadius: "75px"
    },
    header: {
        backgroundColor: "black",
        textAlign: "center"
    },
    title: {
        fontSize: 40,
        color: "white",
        margin: 10
    },
    page: {
        display: 'flex',
        height: '100%'
    }
});

export default HomeScreen;