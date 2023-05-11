import Head from 'next/head'
import Image from 'next/image'
import { Inter } from 'next/font/google'
import * as React from 'react';
import { NavBar } from '../src/components/NavBar';
import { SignUpPage } from '../src/views/SignUpPage';

export default function Home() {
  return (
     <div>
      <NavBar></NavBar>
    </div>
  )
}