/*
kodowanie Huffmana (ang. Huffman Coding) - najłatwiejsza metoda kompresji bezstratnej (informację
zapisujemy za pomocą mniejszej liczby bitów i możemy ją odtworzyć do takiej samej postaci).
Używa się go przy MP3 i JPEG. Jest to przykład algorytmu zachłannego.

algorytm zachłanny - w celu znalezienia najlepszego rozwiązania w każdym kroku dokonuje zachłannego
(wydającego się w danym momencie najlepszym) wyboru.

algorytm deterministyczny - każdorazowe jego wykonanie daje ten sam wynik dla tego samego wejścia.

Rozwiązanie polega na wyznaczeniu częstotliwości występowania znaków w tekście. Następnie tworzone są
słowa kodowe, których długość jest odwrotnie proporcjonalna do częstotliwości występowania znaku.
Tzn. im częściej dany symbol występuje (może wystąpić) w ciągu danych, tym mniej zajmie bitów.

Kroki algorytmu:
1) Określ częstość dla znaków.
