import Head from 'next/head'
import Image from 'next/image'
import { Inter } from 'next/font/google'
import * as React from 'react';
import { ProjectPage } from '../src/views/ProjectPage';

export default function Home() {
  return (
     <div>
      <ProjectPage></ProjectPage>
    </div>
  )
}