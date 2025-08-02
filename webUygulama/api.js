async function generateActivity() {//HTML'deki veriler js değişkenlerine atanır. 
  const gender = document.getElementById("gender").value;
  const age = document.getElementById("age").value;
  const place = document.getElementById("place").value;
  const number = document.getElementById("number").value;
  const hobby = document.getElementById("hobby").value;

 
  const genderText = gender === "1" ? "Kız" : "Erkek"; //HTML'den gelen value metine çevirilir.

  try { //kendi sunucumuza istek gönderimi yapılır.
    const response = await fetch("http://localhost:5000/generateActivity", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        gender: genderText,
        age: age,
        place: place,
        number: number,
        hobby: hobby
      })
    });

    const data = await response.json();//api'den gelen cevabın HTML sayfası üzerinden kullanıcıya gösterilmesi.
    document.getElementById("response").innerText = data.Activity;
  } catch (error) {//hata yakalama satırları
    console.error("Hata:", error);
    document.getElementById("response").innerText = "Etkinlik oluşturulamadı. Lütfen backend'i kontrol edin.";
  }
}


function clearFields() {//HTML'deki temizle butonu fonksiyonu
        document.getElementById("gender").selectedIndex = 0;
        document.getElementById("age").value = "";
        document.getElementById("place").selectedIndex = 0;
        document.getElementById("number").value = "";
        document.getElementById("hobby").value = "";
        document.getElementById("response").innerHTML = "";
}

