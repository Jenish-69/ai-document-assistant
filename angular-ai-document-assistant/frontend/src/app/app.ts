import { Component, ChangeDetectorRef } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { HttpClient } from '@angular/common/http';
import { HttpClientModule } from '@angular/common/http';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-root',
  imports: [FormsModule, HttpClientModule, CommonModule],
  templateUrl: './app.html',
  styleUrl: './app.css'
})
export class App {

  constructor(private http: HttpClient, private cdr: ChangeDetectorRef) {}

  question = '';
  answer = '';
  isLoading = false;
  listeningMessage = '';
  mediaRecorder: any;
  audioChunks: Blob[] = [];

  selectedLanguage = 'English';
  selectedFile: File | null = null;
  uploadMessage = '';
  extractedText = '';
  totalChunks = 0;

  askAI() {
  this.isLoading = true;
  this.answer = '';

  this.http.post<any>('http://127.0.0.1:8000/ask', {
    question: this.question,
    language: this.selectedLanguage
  }).subscribe({
    next: (response) => {
      this.answer = response.answer || 'No answer found';
      this.isLoading = false;
      this.cdr.detectChanges();
    },
    error: (error) => {
      this.answer = 'Frontend error: ' + error.message;
      this.isLoading = false;
      this.cdr.detectChanges();
    }
  });
}
  speakAnswer() {
  if (!this.answer) {
    return;
  }

  const speech = new SpeechSynthesisUtterance(this.answer);

  speech.lang = 'en-US';
  speech.rate = 1;
  speech.pitch = 1;

  window.speechSynthesis.cancel();
  window.speechSynthesis.speak(speech);
}

    onFileSelected(event: any) {

    this.selectedFile = event.target.files[0];

    const formData = new FormData();

    formData.append('file', this.selectedFile!);

    this.http.post<any>(
      'http://127.0.0.1:8000/upload-pdf',
      formData
    ).subscribe((response) => {

      this.uploadMessage = response.message;
      this.extractedText = response.text;
      this.totalChunks = response.total_chunks;

    });
  }

  async startListening() {

    this.listeningMessage = 'Recording... speak now 🎤';

    const stream = await navigator.mediaDevices.getUserMedia({ audio: true });

    this.mediaRecorder = new MediaRecorder(stream);
    this.audioChunks = [];

    this.mediaRecorder.ondataavailable = (event: any) => {
      this.audioChunks.push(event.data);
    };

    this.mediaRecorder.onstop = () => {
      const audioBlob = new Blob(this.audioChunks, { type: 'audio/wav' });

      // We'll add the backend call later
      console.log(audioBlob);
    };

    this.mediaRecorder.start();

    setTimeout(() => {
      this.mediaRecorder.stop();
      this.listeningMessage = 'Converting speech to text...';
      this.cdr.detectChanges();
    }, 5000);
  }

}